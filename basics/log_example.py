def main() -> None:
    import logging

    logging.debug("Debugging information")
    logging.info("Informational message")
    logging.warning("Warning:config file %s not found", "server.conf")
    logging.error("Error occurred")
    logging.critical("Critical error -- shutting down")


if __name__ == "__main__":
    main()
