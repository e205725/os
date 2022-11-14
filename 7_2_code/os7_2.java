import java.util.Enumeration;
import java.net.NetworkInterface;
import java.net.InetAddress;

public class os7_2 {
    public static void main(String[] args) {
        try {
            Enumeration interfaces = NetworkInterface.getNetworkInterfaces();
            while (interfaces.hasMoreElements()) {
                NetworkInterface networkInterface = (NetworkInterface)interfaces.nextElement();
                System.out.println("network interface"+":"+networkInterface.getName());
                Enumeration addresses = networkInterface.getInetAddresses();
                while (addresses.hasMoreElements()) {
                    InetAddress address = (InetAddress)addresses.nextElement();
                    System.out.println("        " + "address " + address.getHostAddress());
                }
            }
        }
        catch (Exception e) {
            System.err.println(e);
        }
    }
}
