import React from "react";
import { OmniAgentAction } from "#/types/core/actions";
import { isOmniAgentAction } from "#/types/core/guards";
import { ChatMessage } from "../chat-message";

const hasThoughtProperty = (
  obj: Record<string, unknown>,
): obj is { thought: string } => "thought" in obj && !!obj.thought;

interface ObservationPairEventMessageProps {
  event: OmniAgentAction;
}

export function ObservationPairEventMessage({
  event,
}: ObservationPairEventMessageProps) {
  if (!isOmniAgentAction(event)) {
    return null;
  }

  if (hasThoughtProperty(event.args) && event.action !== "think") {
    return (
      <div>
        <ChatMessage type="agent" message={event.args.thought} />
      </div>
    );
  }

  return null;
}
