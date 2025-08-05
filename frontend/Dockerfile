FROM node:18
WORKDIR /app
COPY ./public ./public
COPY ./src ./src
RUN npm install -g create-react-app && npx create-react-app . --template cra-template
RUN npm install
RUN npm run build
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
