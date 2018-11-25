package application.logic;

public class ScriptHandler {

	public static void runPythonScript(String scriptName, String arguments)
	{

		try
		{
			System.out.println("started");
			//Process p = Runtime.getRuntime().exec("python "+ "C:\\Users\\Raivo Koot\\Documents\\GitHub\\Oxford-Hackathon\\model_request_prediction\\property_evaluator.py 4 sheffield 200 300 1");
		
			Runtime.getRuntime().exec(new String[] { "cmd.exe", "/c", "C:\\Users\\Raivo Koot\\Documents\\GitHub\\Oxford-Hackathon\\UserInterface\\AestheticallyPleasing\\src\\application\\logic\\start_python_scripts.bat" } );
			
			System.out.println("finished");
		} catch (Exception e)
		{
			e.printStackTrace();
		}

	}

}
