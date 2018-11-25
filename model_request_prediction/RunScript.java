
public class RunScript {

  public static void runPythonScript(String scriptName, String arguments){
    try{

      Process p = Runtime.getRuntime().exec("python " + scriptName +" "+arguments);
    } catch(Exception e){
      System.out.println(e);
    }
  }
}
