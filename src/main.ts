import Server from "./Server";

const server = new Server(process.env.PORT);
server.initServer();