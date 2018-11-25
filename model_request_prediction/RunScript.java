
public class RunScript {

  public static void runPythonScript(String scriptName){
    try{
      Process p = Runtime.getRuntime().exec("python " + scriptName);
    } catch(Exception e){
      System.out.println(e);
    }
  }
}
