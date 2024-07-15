using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.IO;
using System.Reflection;
using System.Configuration;
using System.Threading;
using OpenQA.Selenium.Support.UI;

namespace OnlineShoePortal
{
    [TestClass]
    public class TS01_UserRegistration
    {
        public static WebDriver driver { get; set; }
        [TestMethod]
        public void TC01_UserReg_ErrValidation()
        {
            var chromeOptions = new ChromeOptions();
            chromeOptions.AddArgument("-no-sandbox");
            driver = new ChromeDriver(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), chromeOptions);
            //driver.Navigate().GoToUrl(https://anupdamoda.github.io/AceOnlineShoePortal/");
            driver.Navigate().GoToUrl(ConfigurationManager.AppSettings["URL"]);

            driver.FindElement(By.CssSelector("#menuToggle > input[type=checkbox]")).Click();
            /* If any new item is added to menu, then it might change the value of nth-child, hence replacing statement with LinkText
             * driver.FindElement(By.CssSelector("#menu > a:nth-child(2) > li")).Click();
             */
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.LinkText("Sign In Portal")).Click();

            var txtbx_userlength = driver.FindElements(By.Id("usr")).Count;
            Assert.AreEqual(1, txtbx_userlength);

            var txtbx_pwdlength = driver.FindElements(By.Id("pwd")).Count;
            Assert.AreEqual(1, txtbx_pwdlength);

            var loginButton = driver.FindElements(By.XPath("//input[@value='Login']")).Count;
            Assert.AreEqual(1, loginButton);

            var btnRegistration = driver.FindElements(By.Id("NewRegistration")).Count;
            Assert.AreEqual(1, btnRegistration);

            driver.FindElement(By.Id("NewRegistration")).Click();

            SelectElement drpSalutation = new SelectElement(driver.FindElement(By.Id("Salutation")));
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            drpSalutation.SelectByText(ConfigurationManager.AppSettings["Salutation"]);

            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            var errorMsg = driver.FindElement(By.XPath("//*[@id=\"first_form\"]/div/span")).Text;
            Assert.AreEqual("This field is required", errorMsg);

            driver.FindElement(By.Id("firstname")).SendKeys(ConfigurationManager.AppSettings["FirstName"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            Assert.AreEqual("This field is required", errorMsg);

            driver.FindElement(By.Id("lastname")).SendKeys(ConfigurationManager.AppSettings["LastName"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            Assert.AreEqual("This field is required", errorMsg);

            driver.FindElement(By.Id("emailId")).SendKeys(ConfigurationManager.AppSettings["InvalidEmailAddress"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            var errorMsg2 = driver.FindElement(By.XPath("//*[@id=\"first_form\"]/div/span")).Text;
            Assert.AreEqual("Enter a valid email", errorMsg2);

            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.Id("emailId")).Clear();
            driver.FindElement(By.Id("emailId")).SendKeys(ConfigurationManager.AppSettings["ValidEmailAddress"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            Assert.AreEqual("This field is required", errorMsg);

            driver.FindElement(By.Id("contactNumber")).SendKeys(ConfigurationManager.AppSettings["ContactNumber"]);
            driver.FindElement(By.Id("usr")).SendKeys(ConfigurationManager.AppSettings["Username"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();

            Assert.AreEqual("This field is required", errorMsg);

            driver.FindElement(By.Id("pwd")).SendKeys(ConfigurationManager.AppSettings["Password"]);
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.FindElement(By.XPath("//input[@value='Submit']")).Click();








        }
    }
}
