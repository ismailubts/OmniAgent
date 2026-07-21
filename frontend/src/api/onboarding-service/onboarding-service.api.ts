import { omniAgentApi } from "../omniagent-axios";

export type OnboardingStatusResponse = {
  should_complete_onboarding: boolean;
};

export const onboardingService = {
  getStatus: async (): Promise<OnboardingStatusResponse> => {
    const { data } = await omniAgentApi.get<OnboardingStatusResponse>(
      "/api/onboarding_status",
    );
    return data;
  },
};
