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

import pxToRem from "assets/theme/functions/pxToRem";

export default {
  styleOverrides: {
    root: {
      padding: `${pxToRem(16)} ${pxToRem(24)} ${pxToRem(24)}`,
      marginTop: 0,
      marginBottom: 0,
      position: "relative", // útil se for usar overlays
    },
  },
};

