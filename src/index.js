import PyConnect from "./pyconnect.js";
import remoteTcpClient from "./remoteTcpClient.js";
import tcpClient from "./tcpClient.js";
import dotenv from "dotenv";

dotenv.config();
const ip = process.env.NODE_SERVER_IP;
const port = process.env.NODE_SERVER_PORT;

(async function () {
  await PyConnect.invoke(async function () {
    await new tcpClient().init("127.0.0.1", 7780);
    await new remoteTcpClient().init(ip, port);
  });
})();

process.on("unhandledRejection", (error) => {
  console.error("Unhandled promise rejection:", error);
});
