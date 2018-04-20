FROM node:8

WORKDIR /src
COPY package.json .
RUN npm install && npm install pm2 -g
# secret
# RUN pm2 link zvbn1zgl0toriqz 51275t1gfbrx8mz

COPY . .
