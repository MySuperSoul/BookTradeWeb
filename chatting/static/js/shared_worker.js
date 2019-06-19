const connections = [];
var sharedWebSocket = null;

onconnect = function(e) {
  const port = e.ports[0];
  connections.push(port);
  port.start();
  console.log(connections);

  if (sharedWebSocket !== null) {
    sharedWebSocket = new WebSocket(
      "ws://" + location.host + "/ws/chat/" + location.hash.substring(1) + "/"
    );

    sharedWebSocket.onmessage = function(e) {
      connections.forEach(function(connection) {
        let data = JSON.parse(e.data);
        connection.postMessage(data);
      });
    };
  }

  // sharedWebSocket.send("PING")
};