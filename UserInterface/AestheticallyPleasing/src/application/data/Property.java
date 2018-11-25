package application.data;

import java.util.ArrayList;

public class Property {
	
	private String title;
	private String address;
	private ArrayList<String> image_urls;
	private String property_url;
	private double rating;
	
	public Property() {
		image_urls = new ArrayList<String>();
		rating = 0;
		address = null;
		title = null;
		property_url = null;
	}

	public String getTitle()
	{
		return title;
	}

	public void setTitle(String title)
	{
		this.title = title;
	}

	public String getAddress()
	{
		return address;
	}

	public void setAddress(String address)
	{
		this.address = address;
	}

	public ArrayList<String> getImage_urls()
	{
		return image_urls;
	}

	public void setImage_urls(ArrayList<String> image_urls)
	{
		this.image_urls = image_urls;
	}

	public String getProperty_url()
	{
		return property_url;
	}

	public void setProperty_url(String property_url)
	{
		this.property_url = property_url;
	}

	public double getRating()
	{
		return rating;
	}

	public void setRating(double rating)
	{
		this.rating = rating;
	}
	
	

}
