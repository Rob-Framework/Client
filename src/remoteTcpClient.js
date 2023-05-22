import * as net from "net";
import tcpClient from "./tcpClient.js";

export default class remoteTcpClient {
  static getInstance;
  client;

  async init(ip, port) {
    remoteTcpClient.getInstance = this;

    this.client = new net.Socket();
    this.client.setNoDelay(true);
    this.client.setKeepAlive(true, 5000);
    this.client.connect(port, ip, function () {
      console.log("connected remote");
    });

    this.client.on("data", async function (data) {
      console.log(data);
      const json = data.toString().replace(/'/g, '"');
      const resp = JSON.parse(json);
      const packetId = resp["packetId"];
      const _data = resp["data"];

      console.log("received: " + packetId + " data:", _data);

      if (packetId === 0) {
        tcpClient.getInstance.sendMessage(0, _data);
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
