package EE;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5 {
  // Change input here
  private static String input = "1600 Pennsylvania Ave NW Washington DC 20006"; 

  public static void main(String[] args) {

    long startTime = System.nanoTime();
    // Get memory usage before
    Runtime runtime = Runtime.getRuntime();
    long memBefore = runtime.totalMemory() - runtime.freeMemory();

    String hash = getMd5(input);
    
    long endTime = System.nanoTime();
    // Get memory usage after
    long memAfter = runtime.totalMemory() - runtime.freeMemory();
    long memUsed = memAfter - memBefore;

    long timeTaken = endTime - startTime;

    System.out.println("MD5 Hash: " + hash);
    System.out.println("Time taken: " + timeTaken + " ns");
    System.out.printf("Memory used: %d bytes\n", memUsed);

  }

  public static String getMd5(String input) {

    try {

      MessageDigest md = MessageDigest.getInstance("MD5");
      byte[] messageDigest = md.digest(input.getBytes());

      BigInteger no = new BigInteger(1, messageDigest);

      String hashtext = no.toString(16);
      while (hashtext.length() < 32) {
        hashtext = "0" + hashtext;
      }
      return hashtext;

    } catch (NoSuchAlgorithmException e) {
      throw new RuntimeException(e);
    }
  }
}
