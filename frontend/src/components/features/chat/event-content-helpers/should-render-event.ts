import { OmniAgentAction } from "#/types/core/actions";
import { OmniAgentEventType } from "#/types/core/base";
import {
  isCommandAction,
  isCommandObservation,
  isOmniAgentAction,
  isOmniAgentObservation,
} from "#/types/core/guards";
import { OmniAgentObservation } from "#/types/core/observations";

const COMMON_NO_RENDER_LIST: OmniAgentEventType[] = [
  "system",
  "agent_state_changed",
  "change_agent_state",
];

const ACTION_NO_RENDER_LIST: OmniAgentEventType[] = ["recall"];

const OBSERVATION_NO_RENDER_LIST: OmniAgentEventType[] = ["think"];

export const shouldRenderEvent = (
  event: OmniAgentAction | OmniAgentObservation,
) => {
  if (isOmniAgentAction(event)) {
    if (isCommandAction(event) && event.source === "user") {
      // For user commands, we always hide them from the chat interface
      return false;
    }

    const noRenderList = COMMON_NO_RENDER_LIST.concat(ACTION_NO_RENDER_LIST);
    return !noRenderList.includes(event.action);
  }

  if (isOmniAgentObservation(event)) {
    if (isCommandObservation(event) && event.source === "user") {
      // For user commands, we always hide them from the chat interface
      return false;
    }

    const noRenderList = COMMON_NO_RENDER_LIST.concat(
      OBSERVATION_NO_RENDER_LIST,
    );
    return !noRenderList.includes(event.observation);
  }

  return true;
};

export const hasUserEvent = (
  events: (OmniAgentAction | OmniAgentObservation)[],
) =>
  events.some((event) => isOmniAgentAction(event) && event.source === "user");
