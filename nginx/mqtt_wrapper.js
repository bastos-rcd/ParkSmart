var mqtt;
var reconnectTimeout = 2000;

var host = "192.168.1.86";
var port = 9001;
var path = "/mqtt/";

var useTLS = false;
var username = null;
var password = null;
var cleansession = true;

function MQTTconnect() {
	mqtt = new Paho.MQTT.Client(
		host,
		port,
		path,
		"web_" + parseInt(Math.random() * 100, 10)
	);

	var options = {
		timeout: 3,
		useSSL: useTLS,
		cleanSession: cleansession,
		onSuccess: onConnect,
		onFailure: onFailure,
	};

	mqtt.onConnectionLost = onConnectionLost;
	mqtt.onMessageArrived = onMessageArrived;
	mqtt.connect(options);
}

function onConnect() {
	console.log("Connected to " + host);
	mqtt.subscribe("#");
}

function onConnectionLost(response) {
	setTimeout(MQTTconnect, reconnectTimeout);
}

function onFailure(message) {
	setTimeout(MQTTconnect, reconnectTimeout);
}

function onMessageArrived(message) {
	console.log(message.payloadString);
}
