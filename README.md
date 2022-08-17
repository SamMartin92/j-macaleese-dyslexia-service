# Jennie MacAleese Dyslexia Service

![Multi Device Mockup](documentation/readme/multi-device.PNG)

[Link to live Site](https://jmcds.herokuapp.com/)

JMCDS is a Full Stack site with a centrally owned datatset, user authentication and role based access to mechanisms within the site. It was built for my fourth Portfolio project with [Code Institute](https://codeinstitute.net/ie/) and exists purely for the purpose of displaying my knowledge & capabilities in regards to the project's assessment criteria.

JMCDS is a prototype site to demonstrate what could potentially be used as a site for my sister Jennie MacAleese to offer in the future to potential clients, upon qualification as a Specialist Dyslexia Practitioner. The site advertises the services she may offer and manage bookings. It will also allows users to communicate with her, register with her site and book classes.

## Agile Methodology:

## User Experience:

 * ## Vision:
  The idea and aim of the site is to create a clear and obvious representation of what the business offers to its clients. The site should provide information on the servcies on offer and give users the ability to get in contact with Jennie to avail of the services or send any queries they may have.
  The site should also provide a portal for client's to register, provide their information and submit booking requests for classes at their own convenience, supplying both user and site owner a simple way to manage class scheduling.
  For the site owner, the ability to manage the teaching schedule and handle client bookings through the admin site is necessary for the efficient running of the business. The site has a fully functioning CRUD functionality for both the site admin and users.
 * ## Target Audience:
  Dyslexia affects up to [20% of us](https://dyslexia.yale.edu/dyslexia/dyslexia-faq/). It is one of the most common learning difficulties encountered in society. The target audience for this site would be dyslexia sufferers, those who may think an assessment is worth their time and those who care for dysexia sufferers or who know someone they believe may benefit from the service. 
  The services provided can help those with dyslexia cope with any asociated struggles of the condition in their day-to-day lives, in eductaion, work or at home, and it is those that the site aims to connect with and offer assistance to.
  
  * ## User stories:
  As a site owner:
  1. As a site owner I can advertise my services so that potential clients can learn about my business
  2. As a site owner I can receive contact from users so that I can respond to any queries or requests
  3. As a site owner I can access client bookings so that I can modify or delete if necessary
  4. As a site owner I can accept, cancel and modify bookings so that I can manage my calendar efficiently
  
  As a user:
  1. As a site user I can register an account so that I provide my information & book classes
  2. As a site user I can easily navigate the site so that I can find all the necessary information and features without difficulty
  
  As a returning user:
  1. As a registered user I can access my bookings so that I can modify them and delete them if necessary
  2. As a registered user I can view my previous bookings so that I can see the history of classes I have taken  
 
 * ## UX Plane:
1. ### Strategy:
  - Build a site for JM Dyslecia Services which clearly advertises the services on offer.
  - Build a site which allows clients to contact the buisness owner and avail of the services.
2. ## Scope:
  - Build a site with a centrally owned database to hold record of client data and client actions.
  - Build a booking system with full CRUD functionality.
  - Build a site with integrated authentication to allow clients register and manage their own information and bookings.
  - Build a site with admin functionaity to allow the site owner manage the client database and booking schedules.
  - Build a site through which users can navigate simply and find the information and services they require with ease.
3. ## Structure:
  - Present a visually pleasing site free of clutter with defined sections to present content clearly to the user.
  - Build a site with registered user restricted access.
  - Build a site with responsive design across all devices.
  - Build a site where the user can navigate to any relevant feauture from whichever part of the site they are currently on.
4. ## Skeleton:
    ### Design
  - Before proceeding with the project, I created some simple wireframes in order to give a guide on how to build the home page, services page and view-bookings page.
  - As can be seen in the final site, these were used merely as guides and during the production of the site, certain design decisions were altered.
  - The inclusion of the professional blog was also removed upon consulation with Jennie, who advised a blog would not be part of any future imagined business website.
  - The make-booking and edit-booking pages were to be simple pages with the forms the sole features centered in the screen. I did not feel it necessary to create wireframes for these.
    1. Home Page: 
    ![Home Page Desktop Wireframe](documentation/readme/wireframes/home-page-desktop.PNG)
    ![Home Page Mobile Wireframe](documentation/readme/wireframes/home-page-mobile.PNG)
    
    2. Services Page:
    ![Services Page Wireframe](documentation/readme/wireframes/services.PNG)
    
    3. View Bookings Page:
    ![View Bookings Page Wireframe](documentation/readme/wireframes/view-bookings.PNG)
    ### Database schema:
    There are three data models used in this site:
    1. User:
        - Django built in User model. For authentication and authorisation.
        - This was extended in this project, adding first_name and last_name fields for users to provide on signup
    2. Client:
        - Custom model.
        - The client model hold personal information relevant to the client.
        - It allows the user to provide their own information and a place for the site owner to retrieve this information where necessary.
        - Client can specify whether the service is for them or their child and if the patient is already diagnosed.
    3. Booking:
        - Custom model.
        - The booking model allows site users and admin users to make and manage bookings.
        - Site users can submit booking requests for themselves and admin user can approve, decline, create and delete bookings.
        - Their is 'uniqueconstraint' within the model bewteen the fields 'booking_date' and 'time_slot'. No two instances of bookings can exist with the both same         booking date and time slot which prevents the possibility of double bookings.
     ### Custom Data Models:
     ![Custom Data Models Diagram](documentation/readme/)
 
5. ## Surface:
    - This site should be clear and appear professional.
    - Site should be free of clutter with relevant media where beneficial.
    ### Colour Scheme:
        - The chosen colour scheme can be seen below.
        - It was a design choice to go with a light colour scheme, that presented a calm theme to the user. 
        - The colors chosen were inspired by the site for [email.js.com](emailjs.com). Personally, I like the colour scheme used on this site and so chose to               replicate it in some regard.
        ![Colour Scheme](documentation/readme/)
    ### Typography
        - The font used almost entirely throughout the site is "Helvetica Neue".
        - This is the default font used with bootstrap. Although, it is not an original choice, in decding upon what font to use, I found it difficult to                     accustomise to any other font. Ultimately, i think this font is clear, professional and welcoming and I just decided it was right to leave it as it was. 
        - The other font, used for the Logo of the site, is 'Ubuntu'. This was chosen as it stands out against "Helvetica Neue", without being too much of a                    departure from that design. It feels in keeping with the theme of the site.
  

  
## Technologies

### Languages Used

### Frameworks, Libraries & Programs Used

- https://miniwebtool.com/django-secret-key-generator/
- https://github.com/bitlabstudio/django-booking

## Credits

- Favicon https://iconarchive.com/show/outline-icons-by-iconsmind/Books-icon.html

### Code
- extinding user model https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
- password logins not working when changed to email authentication required. got solution here https://stackoverflow.com/questions/27967319/django-allauth-email-login-always-wrong
