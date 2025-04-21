#Author: Ian Claggett

from obspy import read

"""Collects the list of templates used in the cross_correlate method. 

    Args:
      filepaths: a list of file paths to the rocket launch templates used in cross correlation.

    Returns:
      A list of templates to be used in the cross_correlate method.

    Raises:
      e: loading erro when attempting to load from a path
    """
def collect_templates(filepaths):
    templates = []
    for path in filepaths:
        try:
            templates.append(read(path))
        except Exception as e:
            print(f"[ERROR] Failed to load template '{path}': {e}")
    return templates

"""Collects the list of templates used in the cross_correlate method. 

    Args:
      network: The network code associated with the station being queried
      station: The station code associated with the station being queried
      location: The location code associated with the station being queried
      channel: The channel code associated with the station being queried (can be wildcard *)
      client_code: The client network associated with the station
      startTime: The start time of the correlation
      endTime: The end time of the correlation
      templates: The list of template filepaths used in the detection
      min_freq: The minimum frequency of the bandpass used on the station
      max_freq: The maximum frequency of the bandpass used on the station

    Returns:
      fig: The MatPlot of the seismic waves if the correlator detects anything
        (default None if no rocket launches are detected)
      detections: The list of detection values returned by the cross-correlation
        (default empty list if no detections occur)

    Raises:
      e: loading error when attempting to fetch waveforms or attempt cross-correlation
    """
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
