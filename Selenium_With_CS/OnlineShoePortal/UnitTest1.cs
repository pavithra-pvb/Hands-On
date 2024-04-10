using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.IO;
using System.Reflection;
using System.Configuration;
using System.Threading;

namespace OnlineShoePortal
{
    [TestClass]
    public class UnitTest1
    {
        public static WebDriver driver { get; set; }
        [TestMethod]
        public void TestMethod1()
        {
            var chromeOptions = new ChromeOptions();
            chromeOptions.AddArgument("-no-sandbox");
            driver = new ChromeDriver(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), chromeOptions);
            //driver.Navigate().GoToUrl("https://www.google.co.in/");
            //driver.Navigate().GoToUrl("https://github.com/pavithra-pvb/hands-on");
            driver.Navigate().GoToUrl(ConfigurationManager.AppSettings["URL"]);

            driver.FindElement(By.CssSelector("#menuToggle > input[type=checkbox]")).Click();
            /* If any new item is added to menu, then it might change the value of nth-child, hence replacing statement with LinkText
             * driver.FindElement(By.CssSelector("#menu > a:nth-child(2) > li")).Click();
             */
            Thread.Sleep(2000);
            driver.FindElement(By.LinkText("Sign In Portal")).Click();
            Thread.Sleep(2000);
            driver.FindElement(By.Id("NewRegistration")).Click();
        }
    }
}
