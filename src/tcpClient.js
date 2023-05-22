import * as net from "net";
import remoteTcpClient from "./remoteTcpClient.js";

export default class tcpClient {
  static getInstance;
  client;

  async init(ip, port) {
    tcpClient.getInstance = this;

    this.client = new net.Socket();
    this.client.setNoDelay(true);
    this.client.setKeepAlive(true, 5000);
    this.client.connect(port, ip, function () {
      console.log("connected");
    });

    this.client.on("data", async function (data) {
      const json = data.toString().replace(/'/g, '"');
      const resp = JSON.parse(json);
      const packetId = resp["packetId"];
      const _data = resp["data"];

      if (packetId == 1) {
        remoteTcpClient.getInstance.sendMessage(1, _data);
      }
    });
  }

  send(json) {
    if (this.client !== undefined) {
      this.client.write(json);
    }
  }

  sendMessage(packetId, data) {
    this.send(JSON.stringify({ packetId: packetId, data: data }));
  }
}
