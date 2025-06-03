/*!

=========================================================
* Vision UI Free React - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vision-ui-free-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com/)
* Licensed under MIT (https://github.com/creativetimofficial/vision-ui-free-react/blob/master LICENSE.md)

* Design and Coded by Simmmple & Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

// Vision UI Dashboard React Base Styles
import colors from "assets/theme/base/colors";
// import bgAdmin from "assets/images/body-background.png";

const {
  custom: { backgroundBase, textMain },
  primary,
} = colors;

export default {
  html: {
    scrollBehavior: "smooth",
    backgroundColor: backgroundBase,
  },
  
  body: {
    backgroundColor: backgroundBase,
    color: textMain,
    fontSmoothing: "antialiased",
  },

  "*, *::before, *::after": {
    margin: 0,
    padding: 0,
    boxSizing: "border-box",
  },

  "a, a:link, a:visited": {
    color: textMain,
    textDecoration: "none !important",
    transition: "color 150ms ease-in !important",
  },

  "a:hover, a:focus": {
    color: primary.main,
    textDecoration: "underline",
  },
};