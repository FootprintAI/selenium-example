FROM python:3.9

RUN apt-get update
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libnss3 lsb-release xdg-utils libgbm1

# CHROME VERSION format: ${version}-1, in this case, we use version 96.0.4664.45
# this version should be compatible with chrome driver
ARG CHROME_VERSION="101.0.4951.41-1"
RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN dpkg -i /tmp/chrome.deb  \
  && apt install -fy \
  && rm /tmp/chrome.deb

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
