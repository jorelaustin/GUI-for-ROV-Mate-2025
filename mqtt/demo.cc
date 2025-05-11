#include <iostream>
#include <async_client.h>
#include "mosquitto.h"


using namespace std;
const string SERVER_ADDRESS = "tcp://broker.hivemq.com:1883"; //public MQTT broker
const string CLIENT_ID = "raspberry_pi_publisher";
const string TOPIC = "test/topic";


int main() {
	async_client(SERVER_ADDRESS, CLIENT_ID);

	//set up connection options
	connect_options connOpts;
	connOpts.set_clean_session(true);
	

	try {
		cout << "Connecting to MQTT broker at " << SERVER_ADDRESS << "..." << endl;
	}
	catch(...) {

	}
	return 0;
}
