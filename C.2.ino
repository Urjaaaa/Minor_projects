String inputString = ""; 
boolean stringComplete = false;
String signal = "$GPGLL";
void setup() {
    
    Serial.begin(9600);
    
    inputString.reserve(200);
}

void loop() {
    
    if (stringComplete) {
        String BB = inputString.substring(0, 6);
        if (BB == signal) {
            String LAT = inputString.substring(7, 17);
            int LATperiod = LAT.indexOf('.');
            int LATzero = LAT.indexOf('0');
            if (LATzero == 0) {
                LAT = LAT.substring(1);
            }

            String LON = inputString.substring(20, 31);
            int LONperiod = LON.indexOf('.');
            int LONTzero = LON.indexOf('0');
            if (LONTzero == 0) {
                LON = LON.substring(1);
            }

            Serial.println(LAT+" "+LON);
            //Serial.println();

        }
        inputString = "";
        stringComplete = false;
    }
}

void serialEvent() {
    while (Serial.available()) {
        
        char inChar = (char) Serial.read();
        
        inputString += inChar;
        
        if (inChar == '\n') {
            stringComplete = true;
        }
    }
}
