package selenium_wikipedie;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class wikipedie_test {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		WebDriver d = new FirefoxDriver();
		d.get("https://en.wikipedia.org");
		WebElement link;
		link= d.findElement(By.linkText("English"));
		link.click();
		Thread.sleep(3000);
		WebElement searchBox;
		searchBox = d.findElement(By.id("SearchInput"));
		searchBox.sendKeys("Software");
		searchBox.submit();
		Thread.sleep(5000);
		d.quit();
	}

}
