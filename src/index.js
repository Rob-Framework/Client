import PyConnect from "./pyconnect.js";
import remoteTcpClient from "./remoteTcpClient.js";
import tcpClient from "./tcpClient.js";

const ip = "127.0.0.1";
const port = 7782;

(async function () {
  await PyConnect.invoke(async function () {
    await new tcpClient().init("127.0.0.1", 7780);
    await new remoteTcpClient().init(ip, port);
  });
})();

process.on("unhandledRejection", (error) => {
  console.error("Unhandled promise rejection:", error);
});
