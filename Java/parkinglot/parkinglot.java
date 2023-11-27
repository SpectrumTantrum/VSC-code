package parkinglot;

public class parkinglot {

/**
 * @param charges
 * @return
 */
public static double charges(double charges) {
    double standardcharge = 3;
    double addcharge = 2.50;
    return(standardcharge + (addcharge * time(start, finish)))
}

/**
 * @param start
 * @param finish
 * @return
 */
public static strimg time(String start, string finish) {

    String starthour = start.substring(0,2);
    String startmin = start.substring(3,5);
    String endhour = end.substring(0,2);
    String endmin = end.substring(3,5);

    int hour1 = Integer.parseInt(starthour);
    int min1 = Integer.parseInt(startmin);
    int hour2 = Integer.parseInt(endhour);
    int min2 = Integer.parseInt(endmin);


}
/**
 * @param args
 */
public static void main(String[] args) {
    
    String start, finish;               //time of entry and
                                        //departure in 24 hour
                                        //format e.g. 07:30

    int hours = time(start, finish);    //the function 'time'
                                        //returns the hours parked

    double cost = charges(hours);       //the function 'charges'
                                        //returns the cost of
                                        //parking

    System.out.println("Cost of parking = $" + cost);

}
}
