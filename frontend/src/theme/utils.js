export const pxToRem = (px) => `${px / 16}rem`;

export const gradient = (start, end) =>
  `linear-gradient(to right, ${start}, ${end})`;
