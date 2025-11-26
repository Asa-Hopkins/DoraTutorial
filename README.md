A repository for the Dora workshop I'm running on 26/11/2025

# Getting started
I'm assuming you have Python installed from the Python workshop, so the easiest way to install `dora` is to use `pip`.
This can be done in two parts. The two parts are installed with
`pip install dora-rs-cli`
and
`pip install dora-rs`

We also need `cv2` and `numpy` but I think they should already be installed. If not, then it's just
`pip install opencv-python numpy`

After that, clone this repo and open a terminal inside one of the example folders. To run one of the examples, you first need to start the `dora` server with
`dora up`
Then, run the nodes with
`dora start {filename}.yml`
where `{filename}` is replaced with the name of your yaml file.

A useful tool is `dora graph` which will parse a .yml file and draw a graph of the connections. This can be useful for debugging.
