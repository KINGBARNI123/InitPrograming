<!DOCTYPE html>
<html lang="en">

<body>
 <h2> OWASP Top 10 Vulnerabilities </h2> 
 <p1>The OWASP Top 10 is a list of the 10 most common web application security risks. By writing code and performing<br>
      robust testing with these risks in mind,  developers can create secure applications that keep their users’ <br>
      confidential data safe from attackers.</p1>  <br>

 <h3>What Is OWASP? </h3> 
 <p1>OWASP, or the Open Web Application Security Project, is a nonprofit organization focused on software security.<br>
      Their projects include a number of open-source software development programs and toolkits, local chapters and<br>
       conferences, among other things. One of their projects is the maintenance of the OWASP Top 10,a list of the <br>
       top 10 security risks faced by web applications.</p1>  

 <h1> OWASP Top 10 Vulnerabilities</h1> 
  

 <h3>1. Injection </h3> 
 <p1>Injection occurs when an attacker exploits insecure code to insert (or inject) their own code into a program.<br>
      Because the program is unable to determine code inserted in this way from its own code, attackers are able <br>
      to use injection attacks to access secure areas and confidential information as though they are trusted <br>
      users. Examples of injection include SQL injections, command injections, CRLF injections, and LDAP injections.<br>
      Application security testing can reveal injection flaws and suggest remediationtechniques such as stripping <br>
      special characters from user input or writing parameterized SQL queries.</p1>  

 <h3> 2. Broken Authentication</h3> 
 <p1>Incorrectly implemented authentication and session management calls can be a huge security risk. If attackers<br>
     notice these vulnerabilities, they may be able to easily assume legitimate users' identities.Multifactor<br>
     authentication is one way to mitigate broken authentication. Implement DAST and SCA scans to detect and<br>
     remove issues with implementation errors before code is deployed.</p1>  

 <h3>3. Sensitive Data Exposure </h3> 
 <p1>APIs, which allow developers to connect their application to third-party services like Google Maps, are great<br>
      time-savers. However, some APIs rely on insecure data transmission methods, which attackers can exploit to<br>
       gain access to usernames, passwords, and other sensitive information.Data encryption, tokenization, proper <br>
       key management, and disabling response caching can all help reduce the risk of sensitive data exposure.</p1>  

 <h3>4. XML External Entities </h3> 
 <p1> This risk occurs when attackers are able to upload or include hostile XML content due to insecure code<br>
     , integrations, or dependencies. An SCA scan can find risks in third-party components with known vulnerabilities <br>
     and will warn you about them. Disabling XML external entity processing also reduces the likelihood of an XML entity attack. </p1>  

 <h3> 5. Broken Access Control</h3> 
 <p1>If authentication and access restriction are not properly implemented, it's easy for attackers to take whatever they want. <br>
     With broken access control flaws, unauthenticated or unauthorized users may have access to sensitive files and systems,<br>
      or even user privilege settings. Configuration errors and insecure access control practices are hard to detect as automated<br>
       processes cannot always test for them. Penetration testing can detect missing authentication, but other methods must be used <br>
       to determine configuration problems. Weak access controls and issues with credentials management are preventable with secure<br>
        coding practices, as well as preventative measures like locking down administrative accounts and controls and using<br>
         multi-factor authentication.</p1>  

 <h3>6. Security Misconfiguration </h3> 
 <p1>Just like misconfigured access controls, more general security configuration errors are huge risks that give attackers quick, easy<br>
      access to sensitive data and site areas.<br>
    
    </p1>  

 <h3>7. Cross-Site Scripting </h3> 
 <p1>With cross-site scripting, attackers take advantage of APIs and DOM manipulation to retrieve data from or send commands to your<br>
      application. Cross-site scripting widens the attack surface for threat actors, enabling them to hijack user accounts, access browser<br>
       histories, spread Trojans and worms, control browsers remotely, and more.Training developers in best practices such as data encoding<br>
        and input validation reduces the likelihood of this risk. Sanitize your data by validating that it’s the content you expect for<br>
         that particular field, and by encoding it for the “endpoint” as an extra layer of protection.</p1>  


 <h3>8. Insecure Deserialization </h3> 
 <p1>Deserialization, or retrieving data and objects that have been written to disks or otherwise saved, can be used to remotely execute code<br>
      in your application or as a door to further attacks. The format that an object is serialized into is either structured or binary text <br>
      through common serialization systems like JSON and XML. This flaw occurs when an attacker uses untrusted data to manipulate an application,<br>
       initiate a denial of service (DoS) attack, or execute unpredictable code to change the behavior of the application.</p1>  



 <h3>9. Using Components with Known Vulnerabilities </h3> 
 <p1>No matter how secure your own code is, attackers can exploit APIs, dependencies and other third-party components if they are not themselves secure.<br>
     A static analysis accompanied by a software composition analysis can locate and help neutralize insecure components in your application. Veracode’s<br>
      static code analysis tools can help developers find such insecure components in their code before they publish an application.<br>
    </p1>  


 <h3>10. Insufficient Logging and Monitoring </h3> 
 <p1>Failing to log errors or attacks and poor monitoring practices can introduce a human element to security risks. Threat actors count on a lack of <br>
     monitoring and slower remediation times so that they can carry out their attacks before you have time to notice or react.To prevent issues with<br>
      insufficient logging and monitoring, make sure that all login failures, access control failures, and server-side input validation failures are <br>
      logged with context so that you can identify suspicious activity. Penetration testing is a great way to find areas of your application with <br>
      insufficient logging too. Establishing effective monitoring practices is also essential.</p1>  


 <h5>AUTHOR: BERNABAS MELES
     ETHICAL HACKING </h5> 
 <p1></p1>  


 <h3> </h3> 
 <p1></p1>  
</body>
</html>
