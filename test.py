from obspy import read

# Run this test file to check if Obspy has been installed correctly onto your system.
st = read()  # load example seismogram
st.filter(type='highpass', freq=3.0)
st = st.select(component='Z')
st.plot()