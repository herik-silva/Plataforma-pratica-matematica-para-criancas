"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const routes_1 = __importDefault(require("./Routers/routes"));
const cors_1 = __importDefault(require("cors"));
class Server {
    constructor(newPort) {
        this.port = newPort;
        this.app = (0, express_1.default)();
    }
    initServer(port = this.port) {
        const corsOptions = {
            origin: "*",
            optionsSucessStatus: 200
        };
        this.app.use(express_1.default.static(__dirname + "/pages"));
        this.app.use(routes_1.default);
        this.app.use((0, cors_1.default)(corsOptions));
        this.app.listen(port, () => {
            console.log(`http://localhost:${this.port}`);
        });
    }
}
exports.default = Server;
