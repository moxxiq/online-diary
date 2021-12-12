FROM node:lts-stretch as builder

WORKDIR /frontend
COPY package.json yarn.lock ./
RUN yarn install

ENV PATH="./node_modules/.bin:$PATH"

COPY . ./
RUN yarn run build

FROM nginx:1.19.9-alpine

COPY nginx.conf /etc/nginx/conf.d/configfile.template
COPY --from=builder /frontend/build /usr/share/nginx/html

ENV PORT 8001
ENV HOST 0.0.0.0

EXPOSE 8001
CMD sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/configfile.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"