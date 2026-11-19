# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 7 |
| Low | 10 |
| Informational | 10 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 12    |
| Info | Informational | https://maisplace.net.br | Percentage of responses with status code 2xx | 88 % |
| Info | Informational | https://maisplace.net.br | Percentage of responses with status code 3xx | 4 % |
| Info | Informational | https://maisplace.net.br | Percentage of responses with status code 4xx | 7 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type application/json | 4 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type application/rss+xml | 5 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type text/css | 13 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type text/html | 21 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type text/javascript | 50 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type text/plain | 2 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with content type text/xml | 1 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with method GET | 96 % |
| Info | Informational | https://maisplace.net.br | Percentage of endpoints with method POST | 3 % |
| Info | Informational | https://maisplace.net.br | Count of total endpoints | 158    |
| Info | Informational | https://maisplace.net.br | Percentage of slow responses | 99 % |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Absence of Anti-CSRF Tokens | Medium | Systemic |
| CSP: Failure to Define Directive with No Fallback | Medium | 3 |
| CSP: Wildcard Directive | Medium | 3 |
| CSP: script-src unsafe-inline | Medium | 3 |
| CSP: style-src unsafe-inline | Medium | 3 |
| Content Security Policy (CSP) Header Not Set | Medium | Systemic |
| Vulnerable JS Library | Medium | 1 |
| Cookie No HttpOnly Flag | Low | 3 |
| Cookie without SameSite Attribute | Low | Systemic |
| Cross-Origin-Embedder-Policy Header Missing or Invalid | Low | 3 |
| Cross-Origin-Opener-Policy Header Missing or Invalid | Low | 3 |
| Cross-Origin-Resource-Policy Header Missing or Invalid | Low | 5 |
| In Page Banner Information Leak | Low | 2 |
| Permissions Policy Header Not Set | Low | Systemic |
| Strict-Transport-Security Header Not Set | Low | Systemic |
| Timestamp Disclosure - Unix | Low | Systemic |
| X-Content-Type-Options Header Missing | Low | 4 |
| Authentication Request Identified | Informational | 3 |
| Charset Mismatch | Informational | 1 |
| Cookie Poisoning | Informational | 3 |
| Information Disclosure - Suspicious Comments | Informational | 6 |
| Modern Web Application | Informational | Systemic |
| Non-Storable Content | Informational | Systemic |
| Re-examine Cache-control Directives | Informational | Systemic |
| Session Management Response Identified | Informational | 4 |
| Storable and Cacheable Content | Informational | 5 |
| User Controllable HTML Element Attribute (Potential XSS) | Informational | 8 |




## Alert Detail



### [ Absence of Anti-CSRF Tokens ](https://www.zaproxy.org/docs/alerts/10202/)



##### Medium (Low)

### Description

No Anti-CSRF tokens were found in a HTML submission form.
A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.

* URL: https://maisplace.net.br/hello-world/
  * Node Name: `https://maisplace.net.br/hello-world/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://maisplace.net.br/wp-comments-post.php" method="post" id="commentform" class="comment-form">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "author" "comment_parent" "comment_post_ID" "email" "submit" "url" "wp-comment-cookies-consent" ].`
* URL: https://maisplace.net.br/hello-world/%3Freplytocom=1
  * Node Name: `https://maisplace.net.br/hello-world/ (replytocom)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://maisplace.net.br/wp-comments-post.php" method="post" id="commentform" class="comment-form">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "author" "comment_parent" "comment_post_ID" "email" "submit" "url" "wp-comment-cookies-consent" ].`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form class="woocommerce-form woocommerce-form-login login" method="post" novalidate>`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "_wp_http_referer" "password" "rememberme" "username" "woocommerce-login-nonce" ].`
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form name="lostpasswordform" id="lostpasswordform" action="https://maisplace.net.br/wp-login.php?action=lostpassword" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "redirect_to" "user_login" "wp-submit" ].`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form name="loginform" id="loginform" action="https://maisplace.net.br/wp-login.php" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "redirect_to" "rememberme" "testcookie" "user_login" "user_pass" "wp-submit" ].`

Instances: Systemic


### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

Phase: Implementation
Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.

Phase: Architecture and Design
Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).
Note that this can be bypassed using XSS.

Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
Note that this can be bypassed using XSS.

Use the ESAPI Session Management control.
This control includes a component for CSRF.

Do not use the GET method for any request that triggers a state change.

Phase: Implementation
Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/352.html ](https://cwe.mitre.org/data/definitions/352.html)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ CSP: Failure to Define Directive with No Fallback ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

The Content Security Policy fails to define one of the directives that has no fallback. Missing/excluding them is the same as allowing anything.

* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The directive(s): form-action, base-uri is/are among the directives that do not fallback to default-src.`
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The directive(s): form-action, base-uri is/are among the directives that do not fallback to default-src.`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The directive(s): form-action, base-uri is/are among the directives that do not fallback to default-src.`


Instances: 3

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://web.dev/articles/csp#resource-options ](https://web.dev/articles/csp#resource-options)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ CSP: Wildcard Directive ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The following directives either allow wildcard sources (or ancestors), are not defined, or are overly broadly defined:
script-src, style-src, img-src, connect-src, frame-src, font-src, media-src, object-src, manifest-src, worker-src`
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The following directives either allow wildcard sources (or ancestors), are not defined, or are overly broadly defined:
script-src, style-src, img-src, connect-src, frame-src, font-src, media-src, object-src, manifest-src, worker-src`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `The following directives either allow wildcard sources (or ancestors), are not defined, or are overly broadly defined:
script-src, style-src, img-src, connect-src, frame-src, font-src, media-src, object-src, manifest-src, worker-src`


Instances: 3

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://web.dev/articles/csp#resource-options ](https://web.dev/articles/csp#resource-options)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ CSP: script-src unsafe-inline ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `script-src includes unsafe-inline.`
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `script-src includes unsafe-inline.`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `script-src includes unsafe-inline.`


Instances: 3

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://web.dev/articles/csp#resource-options ](https://web.dev/articles/csp#resource-options)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ CSP: style-src unsafe-inline ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `frame-ancestors 'self';`
  * Other Info: `style-src includes unsafe-inline.`


Instances: 3

### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://web.dev/articles/csp#resource-options ](https://web.dev/articles/csp#resource-options)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-admin/admin-ajax.php
  * Node Name: `https://maisplace.net.br/wp-admin/admin-ajax.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/wc-logs/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/wc-logs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-sitemap.xml
  * Node Name: `https://maisplace.net.br/wp-sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Vulnerable JS Library ](https://www.zaproxy.org/docs/alerts/10003/)



##### Medium (Medium)

### Description

The identified library appears to be vulnerable.

* URL: https://maisplace.net.br/wp-includes/js/dist/vendor/moment.min.js%3Fver=2.30.1
  * Node Name: `https://maisplace.net.br/wp-includes/js/dist/vendor/moment.min.js (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `.version="2.30.1",H=R,_.fn=u,_.min=function(){return Pt("isBefore",[].slice.call(arguments,0))},_.max=function(){return Pt("isAfter",[].slice.call(arguments,0))},_.now=function(){return Date.now?Date.now():+new Date},_.utc=l,_.unix=function(e){return R(1e3*e)},_.months=function(e,t){return fn(e,t,"months")},_.isDate=V,_.locale=ft,_.invalid=I,_.duration=C,_.isMoment=`
  * Other Info: `The identified library moment.js, version 2.30.1 is vulnerable.
CVE-2026-17495
https://github.com/moment/moment/commit/5f7d983c9881e65e07574de9dda3190d99520c07
https://github.com/moment/moment/releases/tag/2.31.0
https://cna.openjsf.org/security-advisories.html
https://github.com/moment/moment/pull/6386
https://github.com/moment/moment/security/advisories/GHSA-4p3w-j4w9-5jqw
`


Instances: 1

### Solution

Upgrade to the latest version of the affected library.

### Reference


* [ https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/ ](https://owasp.org/Top10/2021/A06_2021-Vulnerable_and_Outdated_Components/)


#### CWE Id: [ 1395 ](https://cwe.mitre.org/data/definitions/1395.html)


#### Source ID: 3

### [ Cookie No HttpOnly Flag ](https://www.zaproxy.org/docs/alerts/10010/)



##### Low (Medium)

### Description

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `Set-Cookie: comment_author_8f2941779462998335448f9e94d47edd`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_email_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `Set-Cookie: comment_author_email_8f2941779462998335448f9e94d47edd`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_url_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `Set-Cookie: comment_author_url_8f2941779462998335448f9e94d47edd`
  * Other Info: ``


Instances: 3

### Solution

Ensure that the HttpOnly flag is set for all cookies.

### Reference


* [ https://owasp.org/www-community/HttpOnly ](https://owasp.org/www-community/HttpOnly)


#### CWE Id: [ 1004 ](https://cwe.mitre.org/data/definitions/1004.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cookie without SameSite Attribute ](https://www.zaproxy.org/docs/alerts/10054/)



##### Low (Medium)

### Description

A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.

* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: wordpress_test_cookie`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: wordpress_test_cookie`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `Set-Cookie: comment_author_8f2941779462998335448f9e94d47edd`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_email_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `Set-Cookie: comment_author_email_8f2941779462998335448f9e94d47edd`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-login.php
  * Node Name: `https://maisplace.net.br/wp-login.php ()(log,pwd,redirect_to,rememberme,testcookie,wp-submit)`
  * Method: `POST`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `Set-Cookie: wordpress_test_cookie`
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.

### Reference


* [ https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-cookie-same-site ](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-cookie-same-site)


#### CWE Id: [ 1275 ](https://cwe.mitre.org/data/definitions/1275.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cross-Origin-Embedder-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/hello-world/
  * Node Name: `https://maisplace.net.br/hello-world/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cross-Origin-Opener-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Opener-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/hello-world/
  * Node Name: `https://maisplace.net.br/hello-world/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Opener-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Opener-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.
'same-origin-allow-popups' is considered as less secured and should be avoided.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cross-Origin-Resource-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Resource-Policy header is an opt-in header designed to counter side-channels attacks like Spectre. Resource should be specifically set as shareable amongst different origins.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/hello-world/
  * Node Name: `https://maisplace.net.br/hello-world/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/robots.txt
  * Node Name: `https://maisplace.net.br/robots.txt`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/xmlrpc.php%3Frsd
  * Node Name: `https://maisplace.net.br/xmlrpc.php (rsd)`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 5

### Solution

Ensure that the application/web server sets the Cross-Origin-Resource-Policy header appropriately, and that it sets the Cross-Origin-Resource-Policy header to 'same-origin' for all web pages.
'same-site' is considered as less secured and should be avoided.
If resources must be shared, set the header to 'cross-origin'.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Resource-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-resource-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ In Page Banner Information Leak ](https://www.zaproxy.org/docs/alerts/10009/)



##### Low (High)

### Description

The server returned a version banner string in the response content. Such information leaks may allow attackers to further target specific issues impacting the product and version in use.

* URL: https://maisplace.net.br/wp-content/uploads/wc-logs/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/wc-logs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Apache/2.4.66`
  * Other Info: `There is a chance that the highlight in the finding is on a value in the headers, versus the actual matched string in the response body.`
* URL: https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Apache/2.4.66`
  * Other Info: `There is a chance that the highlight in the finding is on a value in the headers, versus the actual matched string in the response body.`


Instances: 2

### Solution

Configure the server to prevent such information leaks. For example:
Under Tomcat this is done via the "server" directive and implementation of custom error pages.
Under Apache this is done via the "ServerSignature" and "ServerTokens" directives.

### Reference


* [ https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/ ](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-admin/admin-ajax.php
  * Node Name: `https://maisplace.net.br/wp-admin/admin-ajax.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/wc-logs/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/wc-logs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
* [ https://developer.chrome.com/blog/feature-policy/ ](https://developer.chrome.com/blog/feature-policy/)
* [ https://scotthelme.co.uk/a-new-security-header-feature-policy/ ](https://scotthelme.co.uk/a-new-security-header-feature-policy/)
* [ https://w3c.github.io/webappsec-feature-policy/ ](https://w3c.github.io/webappsec-feature-policy/)
* [ https://www.smashingmagazine.com/2018/12/feature-policy/ ](https://www.smashingmagazine.com/2018/12/feature-policy/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Strict-Transport-Security Header Not Set ](https://www.zaproxy.org/docs/alerts/10035/)



##### Low (High)

### Description

HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

* URL: https://maisplace.net.br/cdn-cgi/styles/cf.errors.css
  * Node Name: `https://maisplace.net.br/cdn-cgi/styles/cf.errors.css`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/themes/twentytwentyfive/assets/images/404-image.webp
  * Node Name: `https://maisplace.net.br/wp-content/themes/twentytwentyfive/assets/images/404-image.webp`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-json/wp/v2/users/1
  * Node Name: `https://maisplace.net.br/wp-json/wp/v2/users/1`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-login.php
  * Node Name: `https://maisplace.net.br/wp-login.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)(redirect_to,user_login,wp-submit)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 15

#### Source ID: 3

### [ Timestamp Disclosure - Unix ](https://www.zaproxy.org/docs/alerts/10096/)



##### Low (Low)

### Description

A timestamp was disclosed by the application/web server. - Unix

* URL: https://maisplace.net.br/%3Fs
  * Node Name: `https://maisplace.net.br/ (s)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1795062888`
  * Other Info: `1795062888, which evaluates to: 2026-11-19 04:34:48.`
* URL: https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css%3Fver=7.1.5
  * Node Name: `https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1538461538`
  * Other Info: `1538461538, which evaluates to: 2018-10-02 06:25:38.`
* URL: https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css%3Fver=7.1.5
  * Node Name: `https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1594202899`
  * Other Info: `1594202899, which evaluates to: 2020-07-08 10:08:19.`
* URL: https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css%3Fver=7.1.5
  * Node Name: `https://maisplace.net.br/wp-includes/css/dist/base-styles/admin-schemes.min.css (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1884057971`
  * Other Info: `1884057971, which evaluates to: 2029-09-14 05:26:11.`
* URL: https://maisplace.net.br/%3Fs
  * Node Name: `https://maisplace.net.br/ (s)(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1795062894`
  * Other Info: `1795062894, which evaluates to: 2026-11-19 04:34:54.`

Instances: Systemic


### Solution

Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

### Reference


* [ https://cwe.mitre.org/data/definitions/200.html ](https://cwe.mitre.org/data/definitions/200.html)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: https://maisplace.net.br/cdn-cgi/styles/cf.errors.css
  * Node Name: `https://maisplace.net.br/cdn-cgi/styles/cf.errors.css`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://maisplace.net.br/cdn-cgi/styles/cf.errors.ie.css
  * Node Name: `https://maisplace.net.br/cdn-cgi/styles/cf.errors.ie.css`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://maisplace.net.br/wp-content/themes/twentytwentyfive/assets/images/404-image.webp
  * Node Name: `https://maisplace.net.br/wp-content/themes/twentytwentyfive/assets/images/404-image.webp`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://maisplace.net.br/wp-includes/images/w-logo-gray-white-bg.svg
  * Node Name: `https://maisplace.net.br/wp-includes/images/w-logo-gray-white-bg.svg`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 4

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Authentication Request Identified ](https://www.zaproxy.org/docs/alerts/10111/)



##### Informational (Low)

### Description

The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.

* URL: https://maisplace.net.br/%3Fs
  * Node Name: `https://maisplace.net.br/ (s)(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `login`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=login
userValue=Log in
passwordParam=password
referer=https://maisplace.net.br/?s`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `login`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=login
userValue=Log in
passwordParam=password
referer=https://maisplace.net.br/my-account/`
* URL: https://maisplace.net.br/my-account/lost-password/
  * Node Name: `https://maisplace.net.br/my-account/lost-password/ ()(_wp_http_referer,user_login,wc_reset_password,woocommerce-lost-password-nonce)`
  * Method: `POST`
  * Parameter: `user_login`
  * Attack: ``
  * Evidence: `wc_reset_password`
  * Other Info: `userParam=user_login
userValue=ZAP
passwordParam=wc_reset_password
referer=https://maisplace.net.br/my-account/lost-password/`


Instances: 3

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/)



#### Source ID: 3

### [ Charset Mismatch ](https://www.zaproxy.org/docs/alerts/90011/)



##### Informational (Low)

### Description

This check identifies responses where the HTTP Content-Type header declares a charset different from the charset defined by the body of the HTML or XML. When there's a charset mismatch between the HTTP header and content body Web browsers can be forced into an undesirable content-sniffing mode to determine the content's correct character set.

An attacker could manipulate content on the page to be interpreted in an encoding of their choice. For example, if an attacker can control content at the beginning of the page, they could inject script using UTF-7 encoded text and manipulate some browsers into interpreting that text.

* URL: https://maisplace.net.br/wp-json/oembed/1.0/embed%3Fformat=xml&url=https%253A%252F%252Fmaisplace.net.br%252Fhello-world%252F
  * Node Name: `https://maisplace.net.br/wp-json/oembed/1.0/embed (format,url)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `There was a charset mismatch between the HTTP Header and the XML encoding declaration: [UTF-8] and [null] do not match.`


Instances: 1

### Solution

Force UTF-8 for all text content in both the HTTP header and meta tags in HTML or encoding declarations in XML.

### Reference


* [ https://code.google.com/archive/p/browsersec/wikis/Part2.wiki#Character_set_handling_and_detection ](https://code.google.com/archive/p/browsersec/wikis/Part2.wiki#Character_set_handling_and_detection)


#### CWE Id: [ 436 ](https://cwe.mitre.org/data/definitions/436.html)


#### WASC Id: 15

#### Source ID: 3

### [ Cookie Poisoning ](https://www.zaproxy.org/docs/alerts/10029/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where cookie parameters might be controlled. This is called a cookie poisoning attack, and becomes exploitable when an attacker can manipulate the cookie in various ways. In some cases this will not be exploitable, however, allowing URL parameters to set cookie values is generally considered a bug.

* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `author`
  * Attack: ``
  * Evidence: ``
  * Other Info: `An attacker may be able to poison cookie values through POST parameters. To test if this is a more serious issue, you should try resending that request as a GET, with the POST parameter included as a query string parameter. For example: https://nottrusted.com/page?value=maliciousInput.

This was identified at:

https://maisplace.net.br/wp-comments-post.php

User-input was found in the following cookie:
comment_author_8f2941779462998335448f9e94d47edd=ZAP; expires=Fri, 19 Nov 2027 04:34:51 GMT; Max-Age=31536000; path=/; secure

The user input was:
author=ZAP`
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `email`
  * Attack: ``
  * Evidence: ``
  * Other Info: `An attacker may be able to poison cookie values through POST parameters. To test if this is a more serious issue, you should try resending that request as a GET, with the POST parameter included as a query string parameter. For example: https://nottrusted.com/page?value=maliciousInput.

This was identified at:

https://maisplace.net.br/wp-comments-post.php

User-input was found in the following cookie:
comment_author_email_8f2941779462998335448f9e94d47edd=zaproxy@example.com; expires=Fri, 19 Nov 2027 04:34:51 GMT; Max-Age=31536000; path=/; secure

The user input was:
email=zaproxy@example.com`
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `url`
  * Attack: ``
  * Evidence: ``
  * Other Info: `An attacker may be able to poison cookie values through POST parameters. To test if this is a more serious issue, you should try resending that request as a GET, with the POST parameter included as a query string parameter. For example: https://nottrusted.com/page?value=maliciousInput.

This was identified at:

https://maisplace.net.br/wp-comments-post.php

User-input was found in the following cookie:
comment_author_url_8f2941779462998335448f9e94d47edd=https://zap.example.com; expires=Fri, 19 Nov 2027 04:34:51 GMT; Max-Age=31536000; path=/; secure

The user input was:
url=https://zap.example.com`


Instances: 3

### Solution

Do not allow user input to control cookie names and values. If some query string parameters must be set in cookie values, be sure to filter out semicolon's that can serve as name/value pair delimiters.

### Reference


* [ https://en.wikipedia.org/wiki/HTTP_cookie ](https://en.wikipedia.org/wiki/HTTP_cookie)
* [ https://cwe.mitre.org/data/definitions/565.html ](https://cwe.mitre.org/data/definitions/565.html)


#### CWE Id: [ 565 ](https://cwe.mitre.org/data/definitions/565.html)


#### WASC Id: 20

#### Source ID: 3

### [ Information Disclosure - Suspicious Comments ](https://www.zaproxy.org/docs/alerts/10027/)



##### Informational (Medium)

### Description

The response appears to contain suspicious comments which may help an attacker.

* URL: https://maisplace.net.br/cart/
  * Node Name: `https://maisplace.net.br/cart/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `ourceURL=wc-country-select-js-extra`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//# sourceURL=wc-country-select-js-extra", see evidence field for the suspicious comment/snippet.`
* URL: https://maisplace.net.br/cart/embed/
  * Node Name: `https://maisplace.net.br/cart/embed/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `ourceURL=wc-country-select-js-extra`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//# sourceURL=wc-country-select-js-extra", see evidence field for the suspicious comment/snippet.`
* URL: https://maisplace.net.br/wp-content/plugins/woocommerce/assets/js/jquery-blockui/jquery.blockUI.min.js%3Fver=2.7.0-wc.11.3.0
  * Node Name: `https://maisplace.net.br/wp-content/plugins/woocommerce/assets/js/jquery-blockui/jquery.blockUI.min.js (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `ires jQuery v1.7 or later
 *
 * Examples at: `
  * Other Info: `The following pattern was used: \bLATER\b and was detected in likely comment: "/*!
 * jQuery blockUI plugin
 * Version 2.70.0-2014.11.23
 * Requires jQuery v1.7 or later
 *
 * Examples at: http://malsup.com/", see evidence field for the suspicious comment/snippet.`
* URL: https://maisplace.net.br/wp-includes/js/wp-tooltip.js%3Fver=7.1.5
  * Node Name: `https://maisplace.net.br/wp-includes/js/wp-tooltip.js (ver)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/**
 * @output wp-admin/js/wp-tooltip.js
 *`
  * Other Info: `The following pattern was used: \bADMIN\b and was detected in likely comment: "/**
 * @output wp-admin/js/wp-tooltip.js
 */", see evidence field for the suspicious comment/snippet.`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `//# sourceURL=user-profile-js-extra`
  * Other Info: `The following pattern was used: \bUSER\b and was detected in likely comment: "//# sourceURL=user-profile-js-extra", see evidence field for the suspicious comment/snippet.`
* URL: https://maisplace.net.br/wp-login.php
  * Node Name: `https://maisplace.net.br/wp-login.php ()(log,pwd,redirect_to,rememberme,testcookie,wp-submit)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `//# sourceURL=user-profile-js-extra`
  * Other Info: `The following pattern was used: \bUSER\b and was detected in likely comment: "//# sourceURL=user-profile-js-extra", see evidence field for the suspicious comment/snippet.`


Instances: 6

### Solution

Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.

### Reference



#### CWE Id: [ 615 ](https://cwe.mitre.org/data/definitions/615.html)


#### WASC Id: 13

#### Source ID: 3

### [ Modern Web Application ](https://www.zaproxy.org/docs/alerts/10109/)



##### Informational (Medium)

### Description

The application appears to be a modern web application. If you need to explore it automatically then the Client Spider may well be more effective than the standard one.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="https://maisplace.net.br" target="_self" rel="home" aria-current="page">MaisPlace</a>`
  * Other Info: `Links have been found with a target of '_self' - this is often used by modern frameworks to force a full page reload.`
* URL: https://maisplace.net.br/*%3Fadd-to-cart
  * Node Name: `https://maisplace.net.br/* (add-to-cart)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="https://maisplace.net.br" target="_self" rel="home">MaisPlace</a>`
  * Other Info: `Links have been found with a target of '_self' - this is often used by modern frameworks to force a full page reload.`
* URL: https://maisplace.net.br/wp-content/uploads/wc-logs/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/wc-logs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092" integrity="sha512-UKNk8GbxkABxKcXYuLkO16EleLGUkcvJWtpSNmExE0Too3ZaFAxTscNWEc1OdAv5/BikHawapSCaiD2XCmp+Bw==" data-cf-beacon='{"version":"2024.11.0","token":"a1668b8cd8144741993771030a43f353","r":1,"spa":2}' crossorigin="anonymous"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/vce701823e78c4301a35b7e07294d87301792088814092" integrity="sha512-UKNk8GbxkABxKcXYuLkO16EleLGUkcvJWtpSNmExE0Too3ZaFAxTscNWEc1OdAv5/BikHawapSCaiD2XCmp+Bw==" data-cf-beacon='{"version":"2024.11.0","token":"a1668b8cd8144741993771030a43f353","r":1,"spa":2}' crossorigin="anonymous"></script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://maisplace.net.br/wp-sitemap.xml
  * Node Name: `https://maisplace.net.br/wp-sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="https://maisplace.net.br" target="_self" rel="home">MaisPlace</a>`
  * Other Info: `Links have been found with a target of '_self' - this is often used by modern frameworks to force a full page reload.`

Instances: Systemic


### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3

### [ Non-Storable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are not storable by caching components such as proxy servers. If the response does not contain sensitive, personal or user-specific information, it may benefit from being stored and cached, to improve performance.

* URL: https://maisplace.net.br/wp-admin/
  * Node Name: `https://maisplace.net.br/wp-admin/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-admin/admin-ajax.php
  * Node Name: `https://maisplace.net.br/wp-admin/admin-ajax.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/wc-logs/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/wc-logs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/
  * Node Name: `https://maisplace.net.br/wp-content/uploads/woocommerce_uploads/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://maisplace.net.br/wp-sitemap.xml
  * Node Name: `https://maisplace.net.br/wp-sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``

Instances: Systemic


### Solution

The content may be marked as storable by ensuring that the following conditions are satisfied:
The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable)
The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood)
The "no-store" cache directive must not appear in the request or response header fields
For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response
For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives)
In addition to the conditions above, at least one of the following conditions must also be satisfied by the response:
It must contain an "Expires" header field
It must contain a "max-age" response directive
For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive
It must contain a "Cache Control Extension" that allows it to be cached
It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/hello-world/
  * Node Name: `https://maisplace.net.br/hello-world/`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/robots.txt
  * Node Name: `https://maisplace.net.br/robots.txt`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `max-age=14400`
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://maisplace.net.br/xmlrpc.php%3Frsd
  * Node Name: `https://maisplace.net.br/xmlrpc.php (rsd)`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3

### [ Session Management Response Identified ](https://www.zaproxy.org/docs/alerts/10112/)



##### Informational (Medium)

### Description

The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `wordpress_test_cookie`
  * Other Info: `cookie:wordpress_test_cookie`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `wordpress_test_cookie`
  * Other Info: `cookie:wordpress_test_cookie`
* URL: https://maisplace.net.br/wp-comments-post.php
  * Node Name: `https://maisplace.net.br/wp-comments-post.php ()(author,comment,comment_parent,comment_post_ID,email,submit,url,wp-comment-cookies-consent)`
  * Method: `POST`
  * Parameter: `comment_author_url_8f2941779462998335448f9e94d47edd`
  * Attack: ``
  * Evidence: `comment_author_url_8f2941779462998335448f9e94d47edd`
  * Other Info: `cookie:comment_author_url_8f2941779462998335448f9e94d47edd
cookie:comment_author_email_8f2941779462998335448f9e94d47edd`
* URL: https://maisplace.net.br/wp-login.php
  * Node Name: `https://maisplace.net.br/wp-login.php ()(log,pwd,redirect_to,rememberme,testcookie,wp-submit)`
  * Method: `POST`
  * Parameter: `wordpress_test_cookie`
  * Attack: ``
  * Evidence: `wordpress_test_cookie`
  * Other Info: `cookie:wordpress_test_cookie`


Instances: 4

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/)



#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: https://maisplace.net.br/
  * Node Name: `https://maisplace.net.br/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://maisplace.net.br/robots.txt
  * Node Name: `https://maisplace.net.br/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `max-age=14400`
  * Other Info: ``
* URL: https://maisplace.net.br/sample-page/
  * Node Name: `https://maisplace.net.br/sample-page/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://maisplace.net.br/sitemap.xml
  * Node Name: `https://maisplace.net.br/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://maisplace.net.br/xmlrpc.php%3Frsd
  * Node Name: `https://maisplace.net.br/xmlrpc.php (rsd)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 5

### Solution

Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ User Controllable HTML Element Attribute (Potential XSS) ](https://www.zaproxy.org/docs/alerts/10031/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

* URL: https://maisplace.net.br/wp-login.php%3Faction=lostpassword
  * Node Name: `https://maisplace.net.br/wp-login.php (action)`
  * Method: `GET`
  * Parameter: `action`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/wp-login.php?action=lostpassword

appears to include user input in:
a(n) [form] tag [name] attribute

The user input found was:
action=lostpassword

The user-controlled value was:
lostpasswordform`
* URL: https://maisplace.net.br/wp-login.php%3Freauth=1&redirect_to=https%253A%252F%252Fmaisplace.net.br%252Fwp-admin%252F
  * Node Name: `https://maisplace.net.br/wp-login.php (reauth,redirect_to)`
  * Method: `GET`
  * Parameter: `redirect_to`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/wp-login.php?reauth=1&redirect_to=https%3A%2F%2Fmaisplace.net.br%2Fwp-admin%2F

appears to include user input in:
a(n) [link] tag [href] attribute

The user input found was:
redirect_to=https://maisplace.net.br/wp-admin/

The user-controlled value was:
https://maisplace.net.br/wp-admin/css/forms.min.css?ver=7.1.5`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `_wp_http_referer`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
_wp_http_referer=/my-account/

The user-controlled value was:
/my-account/`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `login`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [button] tag [value] attribute

The user input found was:
login=Log in

The user-controlled value was:
log in`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `password`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
password=ZAP

The user-controlled value was:
zap`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `rememberme`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
rememberme=forever

The user-controlled value was:
forever`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
username=ZAP

The user-controlled value was:
zap`
* URL: https://maisplace.net.br/my-account/
  * Node Name: `https://maisplace.net.br/my-account/ ()(_wp_http_referer,login,password,rememberme,username,woocommerce-login-nonce)`
  * Method: `POST`
  * Parameter: `woocommerce-login-nonce`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

https://maisplace.net.br/my-account/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
woocommerce-login-nonce=63e82b5c4d

The user-controlled value was:
63e82b5c4d`


Instances: 8

### Solution

Validate all input and sanitize output it before writing to any HTML attributes.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 3


