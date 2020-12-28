FROM hivecell/pysyft:v0.2.9

ENV WORKSPACE /workspace

# Setup workspace environment
RUN pip install --no-cache-dir  notebook==6.1.0 jupyter jupyterlab

# Create jupyter notebook workspace
RUN mkdir $WORKSPACE
WORKDIR $WORKSPACE

# Make the image start the jupyer notebook
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
