FROM node:current-slim

# create destination directory
WORKDIR /usr/src/app

# copy the app, note .dockerignore
COPY package.json .
RUN yarn install

# build necessary, even if no static files are needed,
COPY . .
RUN yarn build

# expose 3000 on container
EXPOSE 3000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=3000

# start the app
CMD [ "yarn", "start" ]
