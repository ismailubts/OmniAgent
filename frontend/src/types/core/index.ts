import { OmniAgentAction } from "./actions";
import { OmniAgentObservation } from "./observations";
import { OmniAgentVariance } from "./variances";

/**
 * @deprecated Will be removed once we fully transition to v1 events
 */
export type OmniAgentParsedEvent =
  | OmniAgentAction
  | OmniAgentObservation
  | OmniAgentVariance;
