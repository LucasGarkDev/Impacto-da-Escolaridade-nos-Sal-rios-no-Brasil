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

import colors from "assets/theme/base/colors";
import typography from "assets/theme/base/typography";

const { text } = colors;
const { size } = typography;

export default {
  styleOverrides: {
    root: {
      color: text.main,
      fontSize: size.sm,
      lineHeight: 1.4,
      marginTop: 0,
      marginBottom: 0,
    },
  },
};

