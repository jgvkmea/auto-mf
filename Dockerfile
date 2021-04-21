FROM amazon/aws-lambda-python:3.8

ENV HEADLESS_CHROMIUM=${LAMBDA_TASK_ROOT}/headless-chromium
ENV CHROMEDRIVER=${LAMBDA_TASK_ROOT}/chromedriver

COPY app/app.py ${LAMBDA_TASK_ROOT}
COPY app/requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt
RUN yum install -y unzip
RUN yum install -y libgtk-x11-2.0.so.0 libgdk-x11-2.0.so.0 libXi.so.6 libXcursor.so.1 libXcomposite.so.1 libXtst.so.6 libXss.so.1 libgconf-2.so.4 libasound.so.2 libcups.so.2

RUN curl -L https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip -o ./chromedriver.zip
RUN curl -L https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-57/stable-headless-chromium-amazonlinux-2.zip -o ./headless-chromium.zip
RUN unzip chromedriver.zip -d ${LAMBDA_TASK_ROOT}
RUN unzip headless-chromium.zip -d ${LAMBDA_TASK_ROOT}
RUN rm chromedriver.zip headless-chromium.zip

CMD [ "app.handler" ]
