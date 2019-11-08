ARG NODE_IMAGE_VERSION

FROM node:$NODE_IMAGE_VERSION

WORKDIR /react

COPY . /react/

RUN npm install --silent
RUN npm install react-scripts@3.2.0 -g --silent

EXPOSE 3000

CMD [ "npm", "start" ]