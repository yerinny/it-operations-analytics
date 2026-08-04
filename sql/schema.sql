-- Raw staging table for the synthetic IT support tickets CSV
DROP TABLE IF EXISTS raw_tickets;

CREATE TABLE raw_tickets (
    ticket_id TEXT,
    created_at TEXT,
    customer_id TEXT,
    customer_segment TEXT,
    channel TEXT,
    product_area TEXT,
    issue_type TEXT,
    priority TEXT,
    status TEXT,
    sla_plan TEXT,
    initial_message TEXT,
    agent_first_reply TEXT,
    resolution_summary TEXT,
    resolution_time_hours TEXT,
    reopened TEXT,
    customer_sentiment TEXT,
    csat_score TEXT,
    has_attachment TEXT,
    platform TEXT,
    region TEXT
);


-- Raw staging table for the incident management event log CSV
DROP TABLE IF EXISTS raw_ticket_events;

CREATE TABLE raw_ticket_events (
    case_id TEXT,
    variant TEXT,
    priority TEXT,
    reporter TEXT,
    event_timestamp TEXT,
    event TEXT,
    issue_type TEXT,
    resolver TEXT,
    report_channel TEXT,
    short_description TEXT,
    customer_satisfaction TEXT
);