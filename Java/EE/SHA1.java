package EE;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.time.Instant;
import java.time.temporal.ChronoUnit;

public class SHA1 {

public static String encryptThisString(String input) throws NoSuchAlgorithmException {
MessageDigest md = MessageDigest.getInstance("SHA-1");
byte[] messageDigest = md.digest(input.getBytes());

BigInteger no = new BigInteger(1, messageDigest);
String hashtext = no.toString(16);

while (hashtext.length() < 32) {
  hashtext = "0" + hashtext; 
}

return hashtext;
}

public static void main(String[] args) throws NoSuchAlgorithmException {

String input = "1600 Pennsylvania Ave NW Washington DC 20006";

//get start time
Instant start = Instant.now();
// Get initial memory usage
Runtime runtime = Runtime.getRuntime();
long usedMemory1 = runtime.totalMemory() - runtime.freeMemory();
//caculate SHA-1 hash
String hash = encryptThisString(input);
//get end time
Instant end = Instant.now();
// Get final memory usage   
long usedMemory2 = runtime.totalMemory() - runtime.freeMemory();

// Estimate memory used
long memoryUsed = usedMemory2 - usedMemory1;

long timeElapsed = ChronoUnit.NANOS.between(start, end);

System.out.println("Input: " + input);
System.out.println("Hash: " + hash);
System.out.println("Time taken: " + timeElapsed + " ns");
System.out.println("Estimated memory used: " + memoryUsed + " bytes");

}
}