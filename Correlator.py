#Author: Ian Claggett

from obspy import read

def collect_templates(filepaths):
    templates = []
    for path in filepaths:
        try:
            templates.append(read(path))
        except Exception as e:
            print(f"[ERROR] Failed to load template '{path}': {e}")
    return templates


def cross_correlate(network, station, location, channel, client_code, startTime, endTime, templates, min_freq, max_freq):
    from obspy.clients.fdsn import Client
    import matplotlib.pyplot as plt

    client = Client(client_code)
    fig = None
    detections = []

    try:
        stream = client.get_waveforms(network, station, location, channel, startTime, endTime, attach_response=True)
    except Exception as e:
        print(f"[ERROR] Failed to fetch waveforms: {e}")
        return None, []

    try:
        stream.remove_response(output="VEL")
        stream.filter('bandpass', freqmin=min_freq, freqmax=max_freq)

        from obspy.signal.cross_correlation import correlation_detector
        height = 0.35
        distance = 10

        detections, sims = correlation_detector(stream, templates, height, distance, plot=None)


        if detections:
            for d in detections:
                print("Detection similarity:", d['similarity'] * 200, "%")
            fig = plt.figure(figsize=(8, 4))
            stream.plot(fig=fig, show=False)
        else:
            print("No launches detected at", network)
    except Exception as e:
        print(f"[ERROR] Cross-correlation failed: {e}")
        return None, []

    return fig, detections
