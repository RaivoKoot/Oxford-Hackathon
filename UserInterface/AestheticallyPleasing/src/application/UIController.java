package application;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.layout.VBox;

public class UIController implements Initializable{

	@FXML
	ChoiceBox<String> cmbBedrooms;
	@FXML
	ChoiceBox<String> cmbCity;
	@FXML
	ChoiceBox<String> cmbMinPrice;
	@FXML
	ChoiceBox<String> cmbMaxPrice;
	@FXML
	ChoiceBox<String> cmbRadius;
	
	@FXML
	Button btnSubmit;
	
	@FXML
	VBox vbxPropertyPane;
	
	@Override
	public void initialize(URL location, ResourceBundle resources) {
		
		
		cmbBedrooms.setItems(FXCollections.observableArrayList("1", "2", "3", "4", "5","6","7","8"));
		cmbCity.setItems(FXCollections.observableArrayList("Sheffield", "London", "Manchester"));
		cmbMinPrice.setItems(FXCollections.observableArrayList("100", "200", "300", "350", "400", "500","600","700","800", "900", "1000","1250","1500","1750", "2000"));
		cmbMaxPrice.setItems(FXCollections.observableArrayList("100", "200", "300", "350", "400", "500","600","700","800", "900", "1000","1250","1500","1750", "2000"));
		cmbRadius.setItems(FXCollections.observableArrayList("0.25", "0.5", "1", "3", "5"));
		

	}
	
	
}
