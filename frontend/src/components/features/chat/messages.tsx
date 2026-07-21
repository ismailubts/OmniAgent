import React from "react";
import { OmniAgentAction } from "#/types/core/actions";
import { OmniAgentObservation } from "#/types/core/observations";
import { isOmniAgentAction, isOmniAgentObservation } from "#/types/core/guards";
import { EventMessage } from "./event-message";
import { ChatMessage } from "./chat-message";
import { useOptimisticUserMessageStore } from "#/stores/optimistic-user-message-store";

interface MessagesProps {
  messages: (OmniAgentAction | OmniAgentObservation)[];
  isAwaitingUserConfirmation: boolean;
}

export const Messages: React.FC<MessagesProps> = React.memo(
  ({ messages, isAwaitingUserConfirmation }) => {
    const { getOptimisticUserMessage } = useOptimisticUserMessageStore();
    const optimisticUserMessage = getOptimisticUserMessage();

    const actionHasObservationPair = React.useCallback(
      (event: OmniAgentAction | OmniAgentObservation): boolean => {
        if (isOmniAgentAction(event)) {
          return !!messages.some(
            (msg) => isOmniAgentObservation(msg) && msg.cause === event.id,
          );
        }

        return false;
      },
      [messages],
    );

    return (
      <>
        {messages.map((message, index) => (
          <EventMessage
            key={index}
            event={message}
            hasObservationPair={actionHasObservationPair(message)}
            isAwaitingUserConfirmation={isAwaitingUserConfirmation}
            isLastMessage={messages.length - 1 === index}
          />
        ))}

        {optimisticUserMessage && (
          <ChatMessage type="user" message={optimisticUserMessage} />
        )}
      </>
    );
  },
  (prevProps, nextProps) => {
    // Prevent re-renders if messages are the same length
    if (prevProps.messages.length !== nextProps.messages.length) {
      return false;
    }

    return true;
  },
);

Messages.displayName = "Messages";
