from mcp.server.fastmcp import FastMCP

from zoom_client import create_zoom_meeting

mcp = FastMCP("Zoom MCP")


@mcp.tool()
def create_meeting(
    topic: str,
    start_time: str,
    duration: int,
    user_email: str
):
    """
    Create a Zoom meeting.

    Args:
        topic: Meeting title
        start_time: ISO datetime
        duration: Duration in minutes
        user_email: Host email of the Zoom account to use
    """

    meeting = create_zoom_meeting(
        topic,
        start_time,
        duration,
        user_email
    )

    return {
        "meeting_id": meeting["id"],
        "topic": meeting["topic"],
        "join_url": meeting["join_url"],
        "start_url": meeting["start_url"],
        "password": meeting.get("password"),
        "host_email": meeting.get("host_email")
    }


if __name__ == "__main__":
    print("Starting Zoom MCP Server...")
    print("Available tool: create_meeting")
    mcp.run()