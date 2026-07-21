import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { OmniAgentApiKeyHelp } from "#/components/features/settings/omniagent-api-key-help";

describe("OmniAgentApiKeyHelp", () => {
  it("renders the help link with the provided testId", () => {
    render(<OmniAgentApiKeyHelp testId="oh-api-key-help" />);

    expect(screen.getByTestId("oh-api-key-help")).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "SETTINGS$NAV_API_KEYS" }),
    ).toHaveAttribute("href", "https://github.com/ismailubts/OmniAgent#quickstart");
  });

  it("renders the billing info paragraph with the pricing-details link", () => {
    render(<OmniAgentApiKeyHelp testId="oh-api-key-help" />);

    expect(screen.getByText("SETTINGS$LLM_BILLING_INFO")).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "SETTINGS$SEE_PRICING_DETAILS" }),
    ).toHaveAttribute(
      "href",
      "https://github.com/ismailubts/OmniAgent/blob/main/Development.md",
    );
  });
});
