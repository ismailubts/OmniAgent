import { I18nKey } from "#/i18n/declaration";

export interface Tip {
  key: I18nKey;
  link?: string;
}

export const TIPS: Tip[] = [
  {
    key: I18nKey.TIPS$CUSTOMIZE_MICROAGENT,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/skills/README.md",
  },
  {
    key: I18nKey.TIPS$SETUP_SCRIPT,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
  },
  { key: I18nKey.TIPS$VSCODE_INSTANCE },
  { key: I18nKey.TIPS$SAVE_WORK },
  {
    key: I18nKey.TIPS$SPECIFY_FILES,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
  },
  {
    key: I18nKey.TIPS$HEADLESS_MODE,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
  },
  {
    key: I18nKey.TIPS$CLI_MODE,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
  },
  {
    key: I18nKey.TIPS$GITHUB_HOOK,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/README.md",
  },
  {
    key: I18nKey.TIPS$BLOG_SIGNUP,
    link: "https://github.com/ismailubts/OmniAgent",
  },
  {
    key: I18nKey.TIPS$API_USAGE,
    link: "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
  },
];

export function getRandomTip(): Tip {
  const randomIndex = Math.floor(Math.random() * TIPS.length);
  return TIPS[randomIndex];
}
