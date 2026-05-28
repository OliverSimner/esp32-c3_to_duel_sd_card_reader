#include <SPI.h>
#include <SD.h>

// Define Chip Select (CS) pins
const int sd1_cs = 7;
const int sd2_cs = 10;

void setup() {
  Serial.begin(115200);
  while (!Serial) { ; } // Wait for serial monitor to open

  // Initialize SPI bus with explicit pins
  SPI.begin(4, 5, 6, 7); // SCK=4, MISO=5, MOSI=6, Default SS=7

  Serial.println("Initializing SD Cards...");

  // Initialize SD Card 1 (CS = 7)
  if (!SD.begin(sd1_cs)) {
    Serial.println("Card 1 initialization failed!");
  } else {
    Serial.println("Card 1 initialized successfully.");
    writeFile(SD, "/card1_test.txt", "Hello from SD 1!\n");
  }

  // Initialize SD Card 2 (CS = 10)
  if (!SD.begin(sd2_cs)) {
    Serial.println("Card 2 initialization failed!");
  } else {
    Serial.println("Card 2 initialized successfully.");
    writeFile(SD, "/card2_test.txt", "Hello from SD 2!\n");
  }
}

void loop() {
  // Nothing to do in loop
}

// Function to write data to a file on the specified SD card object
void writeFile(fs::FS &fs, const char *path, const char *message) {
  Serial.printf("Writing file: %s\n", path);

  File file = fs.open(path, FILE_WRITE);
  if(!file) {
    Serial.println("- Failed to open file for writing");
    return;
  }
  if(file.print(message)) {
    Serial.println("- File written");
  } else {
    Serial.println("- Write failed");
  }
  file.close();
}
