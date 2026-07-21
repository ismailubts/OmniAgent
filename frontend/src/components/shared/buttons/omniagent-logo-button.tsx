import { NavLink } from "react-router";
import { useTranslation } from "react-i18next";
import OmniAgentLogo from "#/assets/branding/omniagent-logo.svg?react";
import { I18nKey } from "#/i18n/declaration";
import { StyledTooltip } from "#/components/shared/buttons/styled-tooltip";

export function OmniAgentLogoButton() {
  const { t } = useTranslation();

  const tooltipText = t(I18nKey.BRANDING$OMNIAGENT);
  const ariaLabel = t(I18nKey.BRANDING$OMNIAGENT_LOGO);

  return (
    <StyledTooltip content={tooltipText}>
      <NavLink to="/" aria-label={ariaLabel}>
        <OmniAgentLogo width={46} height={30} />
      </NavLink>
    </StyledTooltip>
  );
}
