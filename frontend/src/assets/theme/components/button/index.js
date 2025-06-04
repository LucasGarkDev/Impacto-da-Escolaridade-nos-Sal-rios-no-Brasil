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

// Vision UI Dashboard React Button Styles
import root from "assets/theme/components/button/root";
import contained from "assets/theme/components/button/contained";
import outlined from "assets/theme/components/button/outlined";
import text from "assets/theme/components/button/text";

export default {
  defaultProps: {
    disableRipple: true,
  },
  styleOverrides: {
    root: { ...root },

    // Contained
    contained: { ...contained.base },
    sizeSmall: { ...contained.small },
    sizeLarge: { ...contained.large },
    containedPrimary: { ...contained.primary },
    containedSecondary: { ...contained.secondary },

    // Outlined
    outlined: { ...outlined.base },
    outlinedPrimary: { ...outlined.primary },
    outlinedSecondary: { ...outlined.secondary },

    // Text
    text: { ...text.base },
    textPrimary: { ...text.primary },
    textSecondary: { ...text.secondary },
  },
};