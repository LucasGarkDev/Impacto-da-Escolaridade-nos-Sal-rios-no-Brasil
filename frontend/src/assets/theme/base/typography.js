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

/**
 * The base typography styles for the Vision UI Dashboard  Material.
 * You can add new typography style using this file.
 * You can customized the typography styles for the entire Vision UI Dashboard  Material using thie file.
 */

// Vision UI Dashboard React Base Styles

import colors from "assets/theme/base/colors";
import "./typography.css";
import pxToRem from "assets/theme/functions/pxToRem";

const { text } = colors;

const baseProperties = {
  fontFamily: '"Rubik", "Helvetica", "Arial", sans-serif',
  fontWeightLight: 300,
  fontWeightRegular: 400,
  fontWeightMedium: 500,
  fontWeightSemiBold: 600, // ADICIONAR
  fontWeightBold: 700,
  fontSizeXXS: pxToRem(10),
  fontSizeXS: pxToRem(12),
  fontSizeSM: pxToRem(14),
  fontSizeRegular: pxToRem(16),
  fontSizeLG: pxToRem(18),
  fontSizeXL: pxToRem(20),
};

const baseHeadingProperties = {
  fontFamily: baseProperties.fontFamily,
  color: text.main,
  fontWeight: baseProperties.fontWeightSemiBold,
};


const baseDisplayProperties = {
  fontFamily: baseProperties.fontFamily,
  color: text.main,
  fontWeight: baseProperties.fontWeightBold, // antes: Light
  lineHeight: 1.15,
};


const typography = {
  fontFamily: baseProperties.fontFamily,
  fontWeightLight: baseProperties.fontWeightLight,
  fontWeightRegular: baseProperties.fontWeightRegular,
  fontWeightMedium: baseProperties.fontWeightMedium,
  fontWeightBold: baseProperties.fontWeightBold,

  h1: {
    fontSize: pxToRem(40),
    lineHeight: 1.25,
    ...baseHeadingProperties,
  },
  h2: {
    fontSize: pxToRem(32),
    lineHeight: 1.3,
    ...baseHeadingProperties,
  },
  h3: {
    fontSize: pxToRem(28),
    lineHeight: 1.375,
    ...baseHeadingProperties,
  },
  h4: {
    fontSize: pxToRem(24),
    lineHeight: 1.375,
    ...baseHeadingProperties,
  },
  h5: {
    fontSize: pxToRem(20),
    lineHeight: 1.375,
    ...baseHeadingProperties,
  },
  h6: {
    fontSize: pxToRem(16),
    lineHeight: 1.625,
    ...baseHeadingProperties,
  },

  subtitle1: {
    fontSize: baseProperties.fontSizeLG,
    fontWeight: baseProperties.fontWeightMedium,
    lineHeight: 1.6,
  },

  subtitle2: {
    fontSize: baseProperties.fontSizeRegular,
    fontWeight: baseProperties.fontWeightMedium,
    lineHeight: 1.6,
  },

  body1: {
    fontSize: baseProperties.fontSizeRegular,
    fontWeight: baseProperties.fontWeightRegular,
    lineHeight: 1.6,
  },

  body2: {
    fontSize: baseProperties.fontSizeSM,
    fontWeight: baseProperties.fontWeightRegular,
    lineHeight: 1.5,
  },

  button: {
    fontSize: baseProperties.fontSizeSM,
    fontWeight: baseProperties.fontWeightMedium,
    textTransform: "none", // antes: uppercase
    lineHeight: 1.4,
  },

  caption: {
    fontSize: baseProperties.fontSizeXS,
    fontWeight: baseProperties.fontWeightRegular,
    lineHeight: 1.25,
  },

  overline: {
    fontSize: baseProperties.fontSizeXS,
    fontWeight: baseProperties.fontWeightRegular,
    letterSpacing: "1px",
    textTransform: "uppercase",
  },

  d1: {
    fontSize: pxToRem(64),
    ...baseDisplayProperties,
  },
  d2: {
    fontSize: pxToRem(56),
    ...baseDisplayProperties,
  },
  d3: {
    fontSize: pxToRem(48),
    ...baseDisplayProperties,
  },
  d4: {
    fontSize: pxToRem(40),
    ...baseDisplayProperties,
  },
  d5: {
    fontSize: pxToRem(32),
    ...baseDisplayProperties,
  },
  d6: {
    fontSize: pxToRem(24),
    ...baseDisplayProperties,
  },

  size: {
    xxs: baseProperties.fontSizeXXS,
    xs: baseProperties.fontSizeXS,
    sm: baseProperties.fontSizeSM,
    regular: baseProperties.fontSizeRegular,
    lg: baseProperties.fontSizeLG,
    xl: baseProperties.fontSizeXL,
  },

  lineHeight: {
    sm: 1.25,
    regular: 1.5,
    lg: 2,
  },
};

export default typography;

